// Test js snippet to extract GA info
if (typeof ga === "function") {
    console.log('ga_version: Google Analytics Recent');
    console.log('ga_ua_code: ' + ga.getAll()[0].get('trackingId'));
    console.log('ga_ua_anonymize_ip: ' + ga.getAll()[0].get('anonymizeIp'));
        }
else if (typeof _sendPageview === "function") {
    console.log('ga_version: Google Analytics Old');
    console.log('ga_ua_code: ' + oCONFIG.GWT_UAID[0]);
    console.log('ga_ua_anonymize_ip: ' + oCONFIG.ANONYMIZE_IP);
}
else {
    console.log('ga_version: No Google Analytics');
    console.log('ga_ua_code: No UA Code');
}
