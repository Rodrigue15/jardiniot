# JardinIoT
Le projet JardinIoT est un jardin autonome. Ce jardin est composé de "buckets" autonomes dans lesquels les plantes sont semées. Un bucket comporte plusieurs sondes mesurant, entre autres, la température et l'humidité. Le bucket, à l'aide du serveur, ajuste l'humidité de la terre, la température et la lumière que reçoit la plante en se basant sur les données reçues par les sondes ainsi que sur différents facteurs, tels l'heure du jour et la date.

Plus de détails sur le projet peuvent être trouvés sur [le Wiki](https://github.com/ClubCedille/jardiniot/wiki "Wiki JardinIoT").

![2018-02-26-175135_3840x1080_scrot](https://user-images.githubusercontent.com/6194072/36700614-4dc76a1c-1b1e-11e8-8d46-71318f757cc2.png)

# Instructions d'installation

1. Vérifiez votre version de Python afin que ce soit la version 2.7 (`python --version`)
2. Installez PlatfromIO à l'aide de `pip`: `pip install -U wheel semantic-version platformio`. Il se peut que vous deviez utiliser `pip2` si Python 3 est installé sur votre ordi.
3. Clonez le projet: `git clone https://github.com/ClubCedille/jardiniot.git`
4. Vous devez installer chaque dépendence (les `lib_deps` qui sont trouvées dans `platformio.ini`) pour que le code puisse compiler:
	* Allez dans `jardiniot-emb/esp/` et exécutez cette commande: `platformio lib install "EspSoftwareSerial" "WiFi" "PubSubClient" "WifiManager" "CmdMessenger"`
	* Allez dans `jardiniot-emb/arduino/` et exécutez cette commande: `platformio lib install "StandardCplusplus" "Timer" "Adafruit Unified Sensor" "DHT sensor library"`
5. Pour flasher le Arduino avec le code, allez dans le fichier `arduino` et exécutez la commande `platformio run --target upload`.
	* Si jamais le logiciel ne peut pas accéder à `/dev/ttyACM0`, il faut faire: `sudo chmod 666 /dev/ttyACM0`.
6. Allez dans le fichier `esp` et faites la même commande pour flasher le ESP8266. Connectez qu'un seul truc à flasher à la fois sur l'ordi.
7. Pour recevoir des `Serial.print()` du Arduino, vous pouvez le faire avec cette commande: `platformio device monitor -p /dev/ttyACM0 -b 9600`

Ceci est un guide général et les commandes peuvent changer. Allez lire [la doc](http://docs.platformio.org/en/latest/installation.html) pour plus de détails.
