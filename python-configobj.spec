%define module	configobj

Summary:	Simple but powerful config file reader and writer
Name:		python-%{module}
Version:	5.0.6
Release:	3
License:	BSD
Group:		Development/Python 
Url:		http://www.voidspace.org.uk/python/configobj.html
Source0:	http://www.voidspace.org.uk/downloads/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python)

Provides:	ConfigObj = %{version}
Provides:	python-ConfigObj = %{version}

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%package -n python2-configobj
Summary:        Simple but powerful config file reader and writer
License:        BSD
Group:		Development/Python

%description -n python2-configobj
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.


%prep
%setup -qc %{module}-%{version}
mv %{module}-%{version} python3
cp -a python3 python2

%build

pushd python3
%__python setup.py build
popd

pushd python2
%__python2 setup.py build
popd

%install
pushd python3
%__python setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{py_puresitedir}/__pycache__
popd

pushd python2
%__python2 setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{py2_puresitedir}/*.pyc
popd

%files
%{py_puresitedir}/*py
%{py_puresitedir}/*.egg-info

%files -n python2-configobj
%{py2_puresitedir}/*py
%{py2_puresitedir}/*.egg-info

