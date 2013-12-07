%define module	configobj

Summary:	Simple but powerful config file reader and writer
Name:		python-%{module}
Version:	4.7.2
Release:	8
License:	BSD
Group:		Development/Python 
Url:		http://www.voidspace.org.uk/python/configobj.html
Source0:	http://www.voidspace.org.uk/downloads/%{module}-%{version}.zip
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
Provides:	ConfigObj = %{version}
Provides:	python-ConfigObj = %{version}

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
# for 4.7.2, it seems the tarball is wrong 
#%%setup -qn %{module}-%{version}
unzip -o %SOURCE0
%setup -D -T -qn %{module}-%{version}
%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%files
%doc docs/*
%{py_puresitedir}/*py
%{py_puresitedir}/*.egg-info

