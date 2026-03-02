set table "cours_5_ELEC0053-2021.powerTimeP.table"; set format "%.5f"
set samples 100.0; plot [x=0:7] 1.5*0.8*cos(40*3.141592654/180)+1.5*0.8*cos(40*3.141592654/180)*cos(2*x)-1.5*0.8*sin(40*3.141592654/180)*sin(2*x)
