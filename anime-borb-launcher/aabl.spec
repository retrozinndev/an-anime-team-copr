%global srcname an-anime-borb-launcher
%global app_name An Anime Borb Launcher

%define install_dir %{_libdir}/%{srcname}
%define icon_dir %{_datadir}/icons
%define apps_dir %{_datadir}/applications
%define app_id moe.launcher.%{srcname}
%define build_output anime-borb-launcher
%define source1_name %{srcname}-%{version}
%define source1_builddir %{_builddir}/%{source1_name}
%define debug_package %{nil}

Name: an-anime-borb-launcher
Version: 1.0.1
Release: 1%{?dist}
License: GPLv3
Summary: An Anime Borb Launcher for Linux with automatic patching and telemetry disabling. App is unmaintened!

URL: https://github.com/an-anime-team/%{srcname}
VCS: {{{ git_dir_vcs }}}
BuildArch: x86_64

Source0: https://github.com/retrozinndev/an-anime-team-copr/archive/refs/heads/main.tar.gz
Source1: https://github.com/an-anime-team/%{srcname}/archive/refs/tags/%{version}.tar.gz

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: git
Requires: glibc
Requires: libwebp
Requires: gtk4
Requires: libcurl
Requires: p7zip
Requires: libadwaita
Requires: xdg-desktop-portal

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
Suggests: mangohud
Suggests: gamescope
Suggests: gamemode

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: rust
BuildRequires: cargo
BuildRequires: git
BuildRequires: libcurl
BuildRequires: libadwaita-devel
BuildRequires: gtk4-devel
BuildRequires: glibc
BuildRequires: glib2
BuildRequires: glib2-devel
BuildRequires: p7zip
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: pango-devel
BuildRequires: rust-gdk4-devel
BuildRequires: tar

%description
%{summary}

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
tar -xvzf %{SOURCE1} --directory %{_builddir}
cd %{source1_builddir}
cargo build --release

%install
# create necessary directories
mkdir -p %{buildroot}/%{install_dir}
mkdir -p %{buildroot}/%{apps_dir}
mkdir -p %{buildroot}/%{icon_dir}
# copy readme and license
cp -f %{source1_builddir}/LICENSE %{buildroot}%{install_dir}
cp -f %{source1_builddir}/README.md %{buildroot}%{install_dir}
# copy binary
cp -f %{source1_builddir}/target/release/%{build_output} %{buildroot}%{install_dir}
# rename binary
mv %{buildroot}%{install_dir}/%{build_output} %{buildroot}%{install_dir}/%{name}
# copy icon
cp -f %{source1_builddir}/assets/images/icon.png %{buildroot}%{icon_dir}/%{app_id}.png
# copy desktop file
cp -f %{source1_builddir}/assets/%{build_output}.desktop %{buildroot}%{apps_dir}

%post
# create link of binary
ln -sf %{install_dir}/%{name} %{_bindir}/%{name}
# apply exec permision to binary
chmod +x %{install_dir}/%{name}

#-- FILES ---------------------------------------------------------------------#
%files
%{install_dir}/*
%{icon_dir}/%{app_id}.png
%{apps_dir}/%{build_output}.desktop

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
{{{ git_dir_changelog }}}
