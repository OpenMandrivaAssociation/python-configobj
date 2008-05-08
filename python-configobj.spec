%define module configobj
%define name   python-%{module}
%define version 4.5.2
%define release %mkrel 1

Name: 	   %{name}
Summary:   Simple but powerful config file reader and writer
Version:   %{version}
Release:   %{release}
Group:	   Development/Python 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 	   http://www.voidspace.org.uk/python/configobj.html
Source0:   %{module}-%{version}.zip
License:   BSD
Provides:  python-ConfigObj = %{version}
Provides:  ConfigObj = %{version}
BuildRequires: python-setuptools
BuildArch: noarch
%py_requires -d

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
rm -rf %buildroot

%__python setup.py install --root=%buildroot --record=INSTALLED_FILES

%clean
rm -rf %buildroot

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs/*.txt
