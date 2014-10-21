%define module	configobj

Summary:	Simple but powerful config file reader and writer
Name:		python-%{module}
Version:	5.0.6
Release:	1
License:	BSD
Group:		Development/Python 
Url:		http://www.voidspace.org.uk/python/configobj.html
Source0:	http://www.voidspace.org.uk/downloads/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
Provides:	ConfigObj = %{version}
Provides:	python-ConfigObj = %{version}

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
%setup -qn %{module}-%{version}
%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{py_puresitedir}/__pycache__

%files
%{py_puresitedir}/*py
%{py_puresitedir}/*.egg-info

