%define module	configobj
%define name	python-%{module}
%define version 4.7.2
%define release %mkrel 2

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
%py_platsitedir/*py
%py_platsitedir/*.egg-info
