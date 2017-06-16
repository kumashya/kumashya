Buildroot: /home/mathamst/svn/grep/grep-2.27
Name: grep
Version: 2.27
Release: 4
Summary: Converted tgz package
License: unknown
Distribution: Slackware/tarball
Group: Converted/unknown
Requires: libc.so.1  = SISCD_2.3
Requires: libc.so.1  = SUNW_0.7
Requires: libc.so.1  = SUNW_1.1
Requires: libc.so.1  = SUNW_1.18
Requires: libc.so.1  = SUNW_1.21
Requires: libc.so.1  = SUNW_1.22
Requires: libc.so.1  = SYSVABI_1.3
Requires: 	libc.so.1 
Requires: 	libm.so.2 

%define _rpmdir ../
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%define _unpackaged_files_terminate_build 0

%description
Converted tgz package

(Converted from a tgz package by alien version 8.93.)

%files
%defattr(-,-,-)
%dir "/usr/"
%dir "/usr/local/"
%dir "/usr/local/pkg/"
%dir "/usr/local/pkg/pkginfo/"
"/usr/local/pkg/pkginfo/grep-2.27"
%dir "/usr/local/sys/"
%dir "/usr/local/sys/grep/"
%dir "/usr/local/sys/grep/2.27/"
%dir "/usr/local/sys/grep/2.27/share/"
%dir "/usr/local/sys/grep/2.27/share/info/"
"/usr/local/sys/grep/2.27/share/info/dir"
"/usr/local/sys/grep/2.27/share/info/grep.info"
%dir "/usr/local/sys/grep/2.27/share/man/"
%dir "/usr/local/sys/grep/2.27/share/man/man1/"
"/usr/local/sys/grep/2.27/share/man/man1/fgrep.1"
"/usr/local/sys/grep/2.27/share/man/man1/grep.1"
"/usr/local/sys/grep/2.27/share/man/man1/egrep.1"
%dir "/usr/local/sys/grep/2.27/bin/"
"/usr/local/sys/grep/2.27/bin/grep"
"/usr/local/sys/grep/2.27/bin/fgrep"
"/usr/local/sys/grep/2.27/bin/egrep"
%dir "/usr/local/sys/grep/2.27/lib/"
"/usr/local/sys/grep/share"
"/usr/local/sys/grep/bin"
"/usr/local/sys/grep/lib"
%dir "/usr/local/bin/"
"/usr/local/bin/grep"
"/usr/local/bin/fgrep"
"/usr/local/bin/egrep"
%dir "/usr/local/lib/"

%post
ln -s -f /usr/local/sys/grep/2.27 /usr/local/sys/grep/current
ln -s -f /usr/local/sys/grep/2.27 /usr/local/sys/grep/latest

