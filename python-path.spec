#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# py.test unit tests

Summary:	Python 2 module wrapper for os.path
Summary(pl.UTF-8):	Moduł Pythona 2 obudowujący os.path
Name:		python-path
Version:	11.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/path-py/
Source0:	https://files.pythonhosted.org/packages/source/p/path.py/path.py-%{version}.tar.gz
# Source0-md5:	de65181c0efc12efc34d1ff1a0b1edfe
Patch0:		%{name}-sphinx.patch
URL:		https://github.com/jaraco/path.py
%if %{with tests} && %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-appdirs
BuildRequires:	python-pytest >= 2.8
BuildRequires:	python-pytest-flake8
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python3-appdirs
BuildRequires:	python3-pytest >= 2.8
BuildRequires:	python3-pytest-flake8
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
BuildRequires:	python3-jaraco.packaging >= 3.2
BuildRequires:	python3-rst.linker >= 1.9
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects
directly.

%description -l pl.UTF-8
path.py implementuje obiekty ścieżek jako instancje pierwszoklasowe,
pozwalające na wykonywanie ogólnych operacji na plikach bezpośrednio
na tych ścieżkach.

%package -n python3-path
Summary:	Python 3 module wrapper for os.path
Summary(pl.UTF-8):	Moduł Pythona 3 obudowujący os.path
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-path
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects
directly.

%description -n python3-path -l pl.UTF-8
path.py implementuje obiekty ścieżek jako instancje pierwszoklasowe,
pozwalające na wykonywanie ogólnych operacji na plikach bezpośrednio
na tych ścieżkach.

%package apidocs
Summary:	Documentation for Python path.py module
Summary(pl.UTF-8):	Dokumentacja modułu Pythona path.py
Group:		Documentation

%description apidocs
Documentation for Python path.py module.

%description apidocs -l pl.UTF-8
Dokumentacja modułu Pythona path.py.

%prep
%setup -q -n path.py-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
%{__python} -m pytest test_path.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
%{__python3} -m pytest test_path.py
%endif
%endif

%if %{with doc}
# disable warnings (-W in SPHINXOPTS) to ignore objects.inv fetching error on builders
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3 \
	SPHINXOPTS=
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/test_path.py*
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/test_path.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/__pycache__/test_path.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/path.py[co]
%{py_sitescriptdir}/path.py-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-path
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/path.py
%{py3_sitescriptdir}/__pycache__/path.cpython-*.py[co]
%{py3_sitescriptdir}/path.py-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
