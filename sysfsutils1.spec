%define fname sysfs
%define lib_name_orig lib%{fname}
%define lib_major 1
%define lib_name %mklibname %{fname} %{lib_major}

Name: 		sysfsutils1
Version: 	1.3.0
Release: 	8
URL:		http://linux-diag.sourceforge.net/
Source0: 	http://prdownloads.sourceforge.net/linux-diag/sysfsutils-%{version}.tar.bz2
License: 	GPL
Group: 		System/Kernel and hardware
Summary: 	Utility suite to enjoy sysfs

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs, a virtual filesystem in Linux kernel versions 2.5+ that
provides a tree of system devices. While a filesystem is a very useful
interface, we've decided to provide a stable programming interface
that will hopefully make it easier for applications to query system devices
and their attributes.

This package currently includes:

- libsysfs: a library for accessing system devices.
- lsbus: a small application to query system bus information.
- systool: an application to view system device information by bus, class,
        and topology.

%package -n	%{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{lib_name_orig}%{lib_major} = %{EVRD}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{lib_name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}%{lib_major}-devel = %{EVRD}

%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{lib_name}-static-devel
Summary:	Static library for developing programs that will use %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version} %{lib_name}-devel = %{version} 
Provides:	%{lib_name_orig}%{lib_major}-static-devel = %{EVRD}

%description -n	%{lib_name}-static-devel
This package contains the static library that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q -n sysfsutils-%version

%build
%configure2_5x
%make

%install
%{makeinstall_std}
rm -rf %{buildroot}{%_bindir/*,%_mandir/man1/*}

%files -n %{lib_name}
%doc AUTHORS README NEWS 
%{_libdir}/libsysfs.so.*

%files -n %{lib_name}-devel
%doc docs/libsysfs.txt
%{_libdir}/libsysfs.so
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h

%files -n %{lib_name}-static-devel
%{_libdir}/libsysfs.a


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3.0-7mdv2010.0
+ Revision: 434255
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.0-6mdv2009.0
+ Revision: 242850
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.3.0-4mdv2008.0
+ Revision: 36203
- rebuild with correct optflags

* Tue Jun 05 2007 Funda Wang <fundawang@mandriva.org> 1.3.0-3mdv2008.0
+ Revision: 35727
- Do not provides libsysfs now
- Import sysfsutils1



* Tue Dec 13 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.3.0-2mdk
- released in contrib as compat library

* Fri Jun 17 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3.0-1mdk
- new release

* Tue Jan 04 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.0-2mdk
- patch 0: fix segfault with vc classq

* Thu Nov 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.0-1mdk
- 1.2.0
- wipe out buildroot in %%install, not %%prep
- don't ship al documents with every subpackage

* Tue Jun 22 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.0-2mdk
- fix download url
- add project url

* Wed Apr 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.0-1mdk
- new release

* Thu Dec 18 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4.0-1mdk
- new release
- remove uneeded patch 0

* Wed Nov 26 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.0-4mdk
- merge latest missing changelog bits :-)

* Wed Nov 26 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.0-3mdk
- reuse newer autoconf macros again
- fix macro abuse
- merge in changelog from contrib sysfsutils

* Tue Nov 25 2003 Nicolas Planel <nplanel@mandrakesoft.com> 0.3.0-2mdk
- Fix provides in libsysfs0.

* Wed Nov 19 2003 Nicolas Planel <nplanel@mandrakesoft.com> 0.3.0-1mdk
- new release
- libification (now there's a share lib)

* Fri Sep 19 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.0-1mdk
- initial release
