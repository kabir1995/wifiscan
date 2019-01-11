import os
import platform
operatingSystem = platform.system()

def __scanLinux(interface="wlan0"):
  rawData = os.popen("iwlist %s scan").read()

  index_start_BSSID = line.find("Address:") + 1
  index_start_RSSI = line.find("Signal level=")

  results = []

  for line in rawData.split('\n'):
    BSSID = line[index_start_BSSID:].strip()
    RSSI = int(line[index_start_RSSI:].strip())
    results.append((BSSID, RSSI))

  return results


def __scanWindows():
  pass

def __scanDarwin():
  rawData = os.popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s").read()
  # print(rawData)

  index_start_BSSID = rawData.find('BSSID')
  index_end_BSSID = rawData.find('RSSI') - 1

  index_start_RSSI = rawData.find('RSSI')
  index_end_RSSi = rawData.find('CHANNEL') - 1

  results = []
  for line in rawData.split('\n')[1:-1]:
    BSSID = line[index_start_BSSID:index_end_BSSID].strip()
    RSSI = int(line[index_start_RSSI:index_end_RSSi].strip())

    results.append((BSSID, RSSI))

  return results


def scan():
  if operatingSystem == 'Linux':
    return __scanLinux()
  elif operatingSystem == 'Windows':
    return __scanWindows()
  elif operatingSystem == 'Darwin':
    return __scanDarwin()
  else:
    print("Unsupported operating system")
    return None

if __name__ == '__main__':
  print(scan())




