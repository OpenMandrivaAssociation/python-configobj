%define module	configobj
%define name	python-%{module}
%define version 4.7.2
%define release %mkrel 5

Name: 	   %{name}
Summary:   Simple but powerful config file reader and writer
Version:   %{version}
Release:   %{release}
License:   BSD
Group:	   Development/Python 
Provides:  python-ConfigObj = %{version}
URL: 	   http://www.voidspace.org.uk/python/configobj.html
Source0:   http://www.voidspace.org.uk/downloads/%{module}-%{version}.zip
Provides:  ConfigObj = %{version}
BuildRequires: python-devel 
BuildRequires: python-setuptools
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
# for 4.7.2, it seems the tarball is wrong 
#%%setup -q -n %{module}-%{version}
unzip -o %SOURCE0
%setup -D -T -q -n %{module}-%{version}
%build
%__python setup.py build

%install
%__rm -rf %buildroot

%__python setup.py install --root=%buildroot

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%doc docs/*
%py_puresitedir/*py
%py_puresitedir/*.egg-info


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 4.7.2-3mdv2011.0
+ Revision: 667925
- mass rebuild

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 4.7.2-2mdv2011.0
+ Revision: 590467
- ILENT: fix build on x86_64
- fix weirdness around the tarball
- do not use obsoleted py_requires macros
- do not use --record as it record uninstalled file
- rebuild for python 2.7

* Tue Mar 02 2010 Lev Givon <lev@mandriva.org> 4.7.2-1mdv2010.1
+ Revision: 513596
- Update to 4.7.2.

* Mon Jan 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.7.0-1mdv2010.1
+ Revision: 489398
- new version

* Mon May 11 2009 Lev Givon <lev@mandriva.org> 4.6.0-1mdv2010.0
+ Revision: 374790
- Update to 4.6.0.

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 4.5.3-2mdv2009.1
+ Revision: 319371
- rebuild for new python

* Fri Jul 25 2008 Lev Givon <lev@mandriva.org> 4.5.3-1mdv2009.0
+ Revision: 249882
- Update to 4.5.3.

* Thu May 08 2008 Lev Givon <lev@mandriva.org> 4.5.2-1mdv2009.0
+ Revision: 204537
- Update to 4.5.2.

* Wed Mar 19 2008 Lev Givon <lev@mandriva.org> 4.4.0-4mdv2008.1
+ Revision: 188763
- Build as noarch package.
  Include license and docs.

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 4.4.0-3mdv2008.1
+ Revision: 171058
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
- fix description-line-too-long

* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.4.0-2mdv2008.1
+ Revision: 158796
- Increase release to build against x86_64
- import python-configobj


* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1.1-1mdv2008.1
- First release for Mandriva.

