chcp 65001
rem VVのエンジンを起動するbatです 

rem パス 
set "run_path=voicevox_engine\windows-cpu"
rem 起動 
.\%run_path%\run.exe --host 0.0.0.0 --allow_origin * --port 50021