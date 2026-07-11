%global tl_name uowthesis
%global tl_revision 19700

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Document class for dissertations at the University of Wollongong
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uowthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A document class for higher degree research theses in compliance with
the specifications of University of Wollongong (UoW) theses in the
"Guidelines for Preparation and Submission of Higher Degree Research
Theses" (March 2006), by the Research Student Centre, Research &
Innovation Division, UoW.

