#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# do not perform "setup.py test"
%bcond_without  setuptools # build without setuptools (for bootstraping)
#
Summary:	Python 2 module to choose appropriate application directories
Summary(pl.UTF-8):	Moduł Pythona 2 do wyboru właściwych katalogów aplikacji
Name:		python-appdirs
Version:	1.4.3
Release:	3
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/appdirs
Source0:	https://files.pythonhosted.org/packages/source/a/appdirs/appdirs-%{version}.tar.gz
# Source0-md5:	44c679904082a2133f5566c8a0d3ab42
URL:		https://github.com/ActiveState/appdirs
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%{?with_setuptools:BuildRequires:      python-setuptools}
%if %{with tests} && "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%{?with_setuptools:BuildRequires:      python3-setuptools}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
appdirs is a module that helps you choose an appropriate:
 - user data dir
 - user config dir
 - user cache dir
 - site data dir
 - site config dir
 - user log dir

%description -l pl.UTF-8
appdirs to moduł pomagający wybrać właściwy katalog dla:
 - danych użytkownika
 - konfiguracji użytkownika
 - pamięci podręcznej użytkownika
 - danych systemu
 - konfiguracji systemu
 - logów użytkownika

%package -n python3-appdirs
Summary:	Python 3 module to choose appropriate application directories
Summary(pl.UTF-8):	Moduł Pythona 3 do wyboru właściwych katalogów aplikacji
Group:		Development/Languages/Python

%description -n python3-appdirs
appdirs is a module that helps you choose an appropriate:
 - user data dir
 - user config dir
 - user cache dir
 - site data dir
 - site config dir
 - user log dir

%description -n python3-appdirs -l pl.UTF-8
appdirs to moduł pomagający wybrać właściwy katalog dla:
 - danych użytkownika
 - konfiguracji użytkownika
 - pamięci podręcznej użytkownika
 - danych systemu
 - konfiguracji systemu
 - logów użytkownika

%prep
%setup -q -n appdirs-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} test/test_api.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} test/test_api.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py_sitescriptdir}/appdirs.py[co]
%{py_sitescriptdir}/appdirs-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-appdirs
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/appdirs.py
%{py3_sitescriptdir}/__pycache__/appdirs.cpython-*.py[co]
%{py3_sitescriptdir}/appdirs-%{version}-py*.egg-info
%endif
