#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flit
Version  : 3.5.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/a8/bc/4bbb98f1ce0ae4e778f3486c39c487a066d69f5ffe4e762c79664dfd5df8/flit-3.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/bc/4bbb98f1ce0ae4e778f3486c39c487a066d69f5ffe4e762c79664dfd5df8/flit-3.5.1.tar.gz
Summary  : A simple packaging tool for simple packages.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-flit-bin = %{version}-%{release}
Requires: pypi-flit-license = %{version}-%{release}
Requires: pypi-flit-python = %{version}-%{release}
Requires: pypi-flit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(flit_core)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
**Flit** is a simple way to put Python packages and modules on PyPI.
It tries to require less thought about packaging and help you avoid common
mistakes.
See `Why use Flit? <https://flit.readthedocs.io/en/latest/rationale.html>`_ for
more about how it compares to other Python packaging tools.

%package bin
Summary: bin components for the pypi-flit package.
Group: Binaries
Requires: pypi-flit-license = %{version}-%{release}

%description bin
bin components for the pypi-flit package.


%package license
Summary: license components for the pypi-flit package.
Group: Default

%description license
license components for the pypi-flit package.


%package python
Summary: python components for the pypi-flit package.
Group: Default
Requires: pypi-flit-python3 = %{version}-%{release}

%description python
python components for the pypi-flit package.


%package python3
Summary: python3 components for the pypi-flit package.
Group: Default
Requires: python3-core
Provides: pypi(flit)
Requires: pypi(docutils)
Requires: pypi(flit_core)
Requires: pypi(requests)
Requires: pypi(tomli)
Requires: pypi(tomli_w)

%description python3
python3 components for the pypi-flit package.


%prep
%setup -q -n flit-3.5.1
cd %{_builddir}/flit-3.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638830324
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flit
cp %{_builddir}/flit-3.5.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flit/12276565e762cd50328b99b71e0343d3d99350a0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flit

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flit/12276565e762cd50328b99b71e0343d3d99350a0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
