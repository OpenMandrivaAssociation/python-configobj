%define module	configobj

Summary:	Simple but powerful config file reader and writer
Name:		python-%{module}
Version:	5.0.9
Release:	1
License:	BSD
Group:		Development/Python 
# Used to be (and might be again in the future)
# http://www.voidspace.org.uk/python/configobj.html
Url:		https://pypi.org/project/configobj/
Source0:	https://pypi.python.org/packages/source/c/configobj/configobj-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildSystem:	python

Provides:	ConfigObj = %{version}
Provides:	python-ConfigObj = %{version}

# Not really, but let's clean up
Obsoletes:	python2-configobj < %{EVRD}

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%files
%{py_puresitedir}/*.*-info
%{py_puresitedir}/configobj
%{py_puresitedir}/validate
