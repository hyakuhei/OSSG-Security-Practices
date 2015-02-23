At the OpenStack Security Group mid-cycle meetup we discussed the rootwrap issue first mentioned on the OpenStack-dev mailing list (http://lists.openstack.org/pipermail/openstack-dev/2015-February/055971.html). We saw similar issues as mentioned on the mailing list:
* The rootwrap filters are overly permissive. Most filters allow running commands as root with no additional filtering on the arguments given to those commands. If a service can run chmod and chown as root with no additional filtering the service might as well run as root.
Little sanitization is done of input to the commands.
* Maintaining the command filters is difficult. We found existing filters that were no longer being used and should have been removed long ago.
* Rootwrap cannot easily express precise semantics of the use cases of privileged commands.

Before even addressing how to better handle completing privileged tasks, we need to determine if the task could be completed in a unprivileged manner with some achitectural changes. For example, where can we use file permissions and ownership instead of running a command as root? Are there files that could be owned by the project's group instead of the root group? It is likely these cases exist in the current code and would be the prefered solution when it works.

We will always have tasks that must be completed as root. We could try to improve rootwrap as it currently stands. At minimum, rootwrap would need a thorough auditing of the rootwrap filters and creation of many new filter classes. Existing CommandFilters need to be replaced with RegExpFilters, but auditing the complex regular expression that result is difficult to do reliably. More likely, every command would need its own filter class to accurately reflect the semantics of the command. That is a lot work that would be better spent on a more comprehensive solution.

For running privileged tasks we need something more robust:
* Provide better and higher level abstractions between the task being performed and the commands being run. This enables better semantic filtering of the arguments being passed to the task. For example, if we need to mount an image or device in a specific filesystem sub-tree the caller does not need to pass the full path of the mount point.
* Takes advantage of available privilege separation mechanisms on Linux. Mechanisms such as process separation and capabilities could be built in. Deployers should be able to develop SELinux and AppArmour policies.
* Moves away from calling external commands where possible.
* Permits sanitization of inputs to privileged tasks. Each external command or library we call in a privileged context will have its own interpretation of its arguments and we need to be able to sanitize that in a task and use specific manner.
* Makes it easy to audit implementations of privileged tasks. Running the command and sanitizing the arguments to the command are security relevant. It is much easier to audit that code if it is in one place per project rather than spread throughout a project's code.
* Permits each project to have project specific tasks and share common tasks with other projects. Every project will only need a limited set of privileged tasks that will vary from project to project. We want to share common tasks so we audit the code once.
* Places minimum burden on developers while still creating better privilege separation.

Our discussions converged on a privileged daemon as the most effective and long-term solution that could meet these goals. The recently proposed (https://review.openstack.org/#/c/155631) privilege separation daemon for neutron is a good start. It could be built upon to meet the above goals. We still need to understand how to better limit usage of general commands. For example, DeleteLink should not be able to delete an arbitrary path. A separate daemon also makes it much easier for deployers to further limit the daemon with SELinux or AppArmour policies as it should be clear from the code what privileges are needed. This also enables us to do direct system calls where appropriate. Whether to directly do system calls or call out to an external program will need to be decided on a case-by-case basis. 

We understand this will impose additional work on developers, but this is work that is necessary in order to better secure OpenStack. The  alternative to doing this work is to accept that some projects, such as nova-compute, just need to run as root and we need to fully audit rootwrap filters for other projects. If deployers want to further restrict run-as-root projects they need to develop their own SELinux or AppAmour policies to better lock down their systems. This is not an ideal situation to be in, but may be a more realistic one without futher changes.

Next steps include:
* In exisitng code, migrate all calls to rootwrap or project specific interfaces to rootwrap to interfaces in a project specific privileged task module. This module would still call rootwrap for the time being, but we could work on doing better interfaces and sanitization before calling rootwrap and then more easily migrate to a future solution.
* Audit existing code to determine if better ways exist that avoid running tasks as root.
* Develop better developer guidance on how to write correct filters for rootwrap.
* Write a Bandit (https://wiki.openstack.org/wiki/Security/Projects#Bandit_Source_Code_Analyzer) plugin to scan code for usage of rootwrap and do gap analysis against.
* Support further work on the neutron privilege separation daemon.
* Regular auditing of any settled upon solution. This is unavoidable.
