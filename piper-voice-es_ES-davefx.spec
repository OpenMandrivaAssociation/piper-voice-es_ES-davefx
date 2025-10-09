Name:		piper-voice-es_ES-davefx
Version:	2023.09.23
Release:	1
Summary:	Spanish male voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/es/es_ES/davefx/medium
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-es
Provides:	piper-voice-es_ES

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
