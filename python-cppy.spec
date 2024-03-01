%global           pypi_name cppy
%define debug_package %nil

Name:             python-cppy
Version:          1.2.1
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/cppy/
Source0:	https://files.pythonhosted.org/packages/c5/7e/6cc5acd93752ee52d2f0423046072a2ce3ae16dfcd44373b9fe2a0222204/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)

%description
A small C++ header library which makes it easier to write Python
extension modules.
The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for
performing common object operations.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install

%files -n python-cppy
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info


