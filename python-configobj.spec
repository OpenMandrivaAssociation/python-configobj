Name: python-configobj
Summary: ConfigObj is a simple but powerful config file reader and writer
Version: 4.4.0
Release: %mkrel 1
Group: Development/Python 
URL: http://www.voidspace.org.uk/python/configobj.html
Source0: configobj_%{version}.orig.tar.gz
License: BSD
Provides: python-ConfigObj = %version
Provides: ConfigObj = %version
BuildRequires: python-setuptools
%py_requires

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file round tripper. Its main feature is that it is very easy to use, with a straightforward programmer's interface and a simple syntax for config files. 

%files
%defattr(-,root,root)
%py_platsitedir/*

#------------------------------------------------------------

%prep
%setup -q -n configobj-%version

%build
python setup.py build

%install
rm -rf %buildroot

python setup.py install --root=%buildroot

%clean
rm -rf %buildroot

