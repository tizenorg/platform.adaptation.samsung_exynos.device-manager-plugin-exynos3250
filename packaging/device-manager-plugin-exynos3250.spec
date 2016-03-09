Name:       device-manager-plugin-exynos3250
Summary:    Device manager plugin exynos3250
Version:    0.0.1
Release:    0
Group:      System/Hardware Adaptation
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}.manifest
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(hwcommon)
BuildRequires:  pkgconfig(glib-2.0)

%description
Device manager plugin exynos 3250


%prep
%setup -q
cp %{SOURCE1} .

%build
%cmake .

make %{?jobs:-j%jobs}

%install
%make_install


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/hw/*.so
%manifest %{name}.manifest
%license LICENSE
