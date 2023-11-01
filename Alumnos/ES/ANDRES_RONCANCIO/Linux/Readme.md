# Linux_Comandos

SOLUCION - Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
# (base) andresrsalamanca@GARS ~ % ls /bin
dd		launchctl	pwd		tcsh
bash		df		link		realpath	test
cat		echo		ln		rm		unlink
chmod		ed		ls		rmdir		wait4path
cp		expr		mkdir		sh		zsh
csh		hostname	mv		sleep
dash		kill		pax		stty
date		ksh		ps		sync
     
  2.Listar todos los archivos del directorio tmp.
# (base) andresrsalamanca@GARS ~ % ls /tmp
com.apple.launchd.XlnKWP5jru	com.google.Keystone
   
  3.Listar todos los archivos del directorio etc que empiecen por t 
# (base) andresrsalamanca@GARS ~ % ls /etc/t*
/etc/ttys    
    
  4.Listar todos los archivos del directorio dev que empiecen por tty.
# andresrsalamanca@GARS ~ % ls /dev/tty*
dev/tty				/dev/ttysc
/dev/tty.Bluetooth-Incoming-Port	/dev/ttysd
/dev/tty.HUAWEIFreeBuds4i		/dev/ttyse
/dev/tty.SamsungSoundbarJ-Series	/dev/ttysf
/dev/ttyp0				/dev/ttyt0
/dev/ttyp1				/dev/ttyt1

 (CONTINUA)...

5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
# andresrsalamanca@GARS ~ % ls /dev/tty*[3]
/dev/ttyp3	/dev/ttyr3	/dev/ttys3	/dev/ttyu3	/dev/ttyw3
/dev/ttyq3	/dev/ttys003	/dev/ttyt3	/dev/ttyv3 
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
# andresrsalamanca@GARS ~ % ls /dev/t*C1  
zsh: no matches found: /dev/t*C1
    
  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.  
# andresrsalamanca@GARS ~ % ls -a
.				.vscode
..				.xonshrc
.CFUserTextEncoding		.zsh_history
.DS_Store			.zsh_sessions
.Trash				.zshrc
.anaconda			Applications
.bash_profile			Declaracion de renta 2022
.conda				Desktop

8.Listar todos los archivos del directorio etc que no empiecen por t.
# andresrsalamanca@GARS ~ % ls /etc/[^t]*

/etc/afpovertcp.cfg
/etc/aliases
/etc/aliases.db
/etc/asl.conf
/etc/auto_home
/etc/auto_master
/etc/autofs.conf
/etc/bashrc
(continua)...

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
# andresrsalamanca@GARS ~ % ls -R /usr
X11		bin		libexec		sbin		standalone
X11R6		lib		local		share

/usr/bin:
AssetCacheLocatorUtil		memory_pressure
AssetCacheManagerUtil		mesg
AssetCacheTetheratorUtil	mg
DeRez				mib2c
GetFileInfo			mib2c-update
IOAccelMemory			mig
IOMFB_FDR_Loader		mkbom
IOSDebug			mkfifo
ResMerger			mklocale
(continua..)

10.Cambiarse al directorio tmp, crear directorio PRUEBA.
# andresrsalamanca@GARS /tmp % cd /tmp && mkdir PRUEBA

  11.Verificar que el directorio actual ha cambiado.
# andresrsalamanca@GARS /tmp % ls
PRUEBA				com.apple.launchd.XlnKWP5jru	com.google.Keystone
  
  12.Mostrar el día y la hora actual.
# andresrsalamanca@GARS /tmp % date
Sun Oct 29 12:02:10 CET 2023  
    
13.Con un solo comando posicionarse en el directorio $HOME.
# andresrsalamanca@GARS ~ % cd
(base) 
    
14.Verificar que se está en él.
# andresrsalamanca@GARS ~ % pwd  
    
15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
# andresrsalamanca@GARS ~ % ls -l
total 0
drwx------@  3 andresrsalamanca  staff    96 Sep 11 19:16 Applications
drwxr-xr-x   9 andresrsalamanca  staff   288 Sep  4 02:28 Declaracion de renta 2022
drwx------+  5 andresrsalamanca  staff   160 Oct 25 09:57 Desktop
drwx------+ 15 andresrsalamanca  staff   480 Oct 26 16:11 Documents
drwx------+ 41 andresrsalamanca  staff  1312 Oct 27 10:43 Downloads
drwx------@ 96 andresrsalamanca  staff  3072 Oct  3 23:51 Library
drwxr-xr-x   5 andresrsalamanca  staff   160 Oct 24 19:11 MDA
    
16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
# andresrsalamanca@GARS ~ % rm -r /tmp/PRUEBA
    

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
cd
(base) andresrsalamanca@GARS ~ % mkdir PRUEBA
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir1
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir2
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir3
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir1/dir11
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir3/dir31
(base) andresrsalamanca@GARS ~ % mkdir ~/PRUEBA/dir3/dir31/dir311 && mkdir ~/PRUEBA/dir3/dir31/dir312

  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
# cp /etc/motd  ~/PRUEBA/mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.
# cp mensaje ~/PRUEBA/dir1 && cp mensaje ~/PRUEBA/dir2 && cp mensaje ~/dir3
ls -R /PRUEBA  
    
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
# andresrsalamanca@GARS ~ % ls -R ~/PRUEBA
dir1	dir2	dir3

/Users/andresrsalamanca/PRUEBA/dir1:
dir11

/Users/andresrsalamanca/PRUEBA/dir1/dir11:

/Users/andresrsalamanca/PRUEBA/dir2:

/Users/andresrsalamanca/PRUEBA/dir3:
dir31

/Users/andresrsalamanca/PRUEBA/dir3/dir31:
dir311	dir312

/Users/andresrsalamanca/PRUEBA/dir3/dir31/dir311:

/Users/andresrsalamanca/PRUEBA/dir3/dir31/dir312: