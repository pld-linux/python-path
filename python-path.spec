
%include	/usr/lib/rpm/macros.python
%define 	module path

Summary:	Functionality wrapper of the os.path module
Summary(pl):	Wraper funkcjonalno¶ci modu³u os.path
Name:		python-path
Version:	2.0.4
Release:	1
License:	Custom (do, what you want)
Group:		Libraries/Python
Source0:	http://www.jorendorff.com/articles/python/path/%{module}.py
# NoSource0-md5: 9ae93736f9845827aed23bcfa0aaa6ea
URL:		http://www.jorendorff.com/articles/python/path/
Requires:	python >= 2.2
BuildRequires:	python >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This module provides a single class that wraps the functionality in
the os.path module. You wouldn't think that would be so helpful, but
in practice I find it much more pleasant to write and to read.

%description -l pl
Modu³ ten udostêpnia pojedyncz± klasê bêd±c± wrapperem na
funkcjonalno¶æ modu³u os.path.

%prep
%setup -q -c -T
cp -f %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/
install %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}.pyc
%{py_sitescriptdir}/%{module}.pyo
