#
# $Id$
#
Summary:	Busybox version suited for Mindi
Name:		mindi-busybox
Version:	1.18.5
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
Buildrequires: gcc
ExcludeArch:	ppc

%description
This package provides a busybox version suited for Mindi.

%prep
%setup -n %name-%{version}

%build
make oldconfig
make busybox

%install
%{__rm}  -rf $RPM_BUILD_ROOT

DESTDIR=${RPM_BUILD_ROOT}%{_libdir}/mindi/rootfs
make CONFIG_PREFIX=$DESTDIR install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE AUTHORS README TODO NEWS
%{_libdir}/mindi



%changelog
* Sun Feb 26 2012 Bruno Cornec <bcornec@mandriva.org> 1.18.5-1mdv2012.0
+ Revision: 780867
- Update to upstream 1.18.5

* Mon Mar 21 2011 Bruno Cornec <bcornec@mandriva.org> 1.18.3-1
+ Revision: 647363
- Fix reference to upstream mindi-busybox tar file
- Update mindi-busybox to upstream 1.18.3

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Wed May 19 2010 Bruno Cornec <bcornec@mandriva.org> 1.7.3-4mdv2010.1
+ Revision: 545308
- Update tag in order to regenerate the package for 2010.1 - No change.

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.7.3-3mdv2010.0
+ Revision: 439808
- rebuild

* Wed Feb 18 2009 Bruno Cornec <bcornec@mandriva.org> 1.7.3-2mdv2009.1
+ Revision: 342579
- Buildrequires fixed (and now tag updated)

* Mon Dec 08 2008 Bruno Cornec <bcornec@mandriva.org> 1.7.3-1mdv2009.1
+ Revision: 311738
-Update to mindi-busybox 1.7.3
- Updated to 1.2.2-3
- Fix a blocking bug in mindi-busybox gentoo's ebuild (Francesco Talamona)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 16 2007 Bruno Cornec <bcornec@mandriva.org> 1.2.2-2mdv2008.0
+ Revision: 27124
- Tag -2 to force a clean update in repositories

* Wed Apr 25 2007 Bruno Cornec <bcornec@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 18034
- Updated to 1.2.2-2
- Improve Gentoo packaging (Linos)
- Updated to 1.2.2-2
- Improve Gentoo packaging (Linos)


* Thu Jan 04 2007 bcornec <bcornec> 1.2.2-1mdv2007.0
+ Revision: 103985
- Updated to 1.2.2
- mindi-busybox version is now extended with the SVN revision (Bruno Cornec)
- Fix a known bug for busybox where -gc-section in makefile + static for link crea tes a buggy busybox with glibc (Bruno Cornec)
- Updated based on busybox 1.2.2 (Bruno Cornec)
- Handles modules back again (Bruno Cornec)
- Fix bug #88 around install conflicts (Bruno Cornec)
- Update packager
- Updated to 1.2.2
- mindi-busybox version is now extended with the SVN revision (Bruno Cornec)
- Fix a known bug for busybox where -gc-section in makefile + static for link crea tes a buggy busybox with glibc (Bruno Cornec)
- Updated based on busybox 1.2.2 (Bruno Cornec)
- Handles modules back again (Bruno Cornec)
- Fix bug #88 around install conflicts (Bruno Cornec)
- Updated to 1.2.2
- mindi-busybox version is now extended with the SVN revision (Bruno Cornec)
- Fix a known bug for busybox where -gc-section in makefile + static for link crea tes a buggy busybox with glibc (Bruno Cornec)
- Updated based on busybox 1.2.2 (Bruno Cornec)
- Handles modules back again (Bruno Cornec)
- Fix bug #88 around install conflicts (Bruno Cornec)
- Updated to 1.2.1
- Creation based on busybox 1.2.1 (Bruno Cornec)
- Remove module management, bunzip2 in config file (Bruno Cornec)
- Import mindi-busybox

* Thu Oct 05 2006 Bruno Cornec <bruno@mondorescue.org> 1.2.1-3.20060mdv
- Updated to 1.2.1
- Creation based on busybox 1.2.1 (Bruno Cornec)
- Remove module management, bunzip2 in config file (Bruno Cornec)

