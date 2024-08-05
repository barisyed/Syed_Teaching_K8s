@echo off
cd %2
%1 -i silent -DUSER_INSTALL_DIR="%3"
