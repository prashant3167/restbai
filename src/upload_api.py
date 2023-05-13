import requests
import json

reqUrl = "http://127.0.0.1:8000/upload"
print(type(open("/Users/rizwan/Downloads/UPC/hack_upc/restbai/lux.jpg", "rb").read()))
post_files = {
  "files":open("/Users/rizwan/Downloads/UPC/hack_upc/restbai/lux.jpg", "rb"),
}
headersList = {
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0",
 "Accept": "*/*",
 "Accept-Language": "en-US,en;q=0.5",
 "Accept-Encoding": "gzip, deflate, br",
 "Access-Control-Request-Method": "POST",
 "Access-Control-Request-Headers": "access-control-allow-headers,access-control-allow-origin",
 "Referer": "http://127.0.0.1:3000/",
 "Origin": "http://127.0.0.1:3000",
 "DNT": "1",
 "Connection": "keep-alive",
 "Sec-Fetch-Dest": "empty",
 "Sec-Fetch-Mode": "cors",
 "Sec-Fetch-Site": "same-site",
 "Pragma": "no-cache",
 "Cache-Control": "no-cache",
 "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A"
}

payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\ntest\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"interior\"\r\n\r\n\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"kitchen\"\r\n\r\nbacksplash,brown_cabinets,dark_brown_cabinets\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"appliances\"\r\n\r\ndishwasher\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"totalBedroom\"\r\n\r\n1\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"totalWashroom\"\r\n\r\n1\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

response = requests.request("POST", reqUrl, files=post_files,data=payload,headers=headersList)

print(response.text)