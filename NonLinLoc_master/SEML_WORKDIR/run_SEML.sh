echo "============"
echo "Developed by ARHAM ZAKKI EDELO"
# PS_VIEWER=ghostview    # Linux, MacOSX
# alias ghostview="open -a Preview"    # MacOSX
# setGMT4    # make sure GMT4 and not GMT5 commands are on path

echo
#echo "Generate the model grid"
#'/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/bin/Vel2Grid' run/SEML_MEQ.in

echo
#echo "Generate and view the travel-time and take-off angle grids "
#'/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/bin/Grid2Time' run/SEML_MEQ.in

echo
echo "Do the event Location "
'/cygdrive/e/SOFTWARE GEOPHYSICS/NonLinLoc/src/bin/NLLoc' run/SEML_MEQ.in

#echo "Visualise the location with Seismicity Viewer"
java -jar SeismicityViewer50.jar loc/SEML.*.*.grid0.loc.hyp

