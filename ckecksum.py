import re

def chksum_nmea(sentence):
    # This is a string, will need to convert it to hex for
    # proper comparsion below
    cksum = sentence[len(sentence) - 2:]
    # print(cksum)

    # String slicing: Grabs all the characters
    # between '$' and '*' and nukes any lingering
    # newline or CRLF
    chksumdata = re.sub("(\n|\r\n)", "", sentence[sentence.find("$") + 1:sentence.find("*")])

    # Initializing our first XOR value
    csum = 0

    # For each char in chksumdata, XOR against the previous
    # XOR'd char.  The final XOR of the last char will be our
    # checksum to verify against the checksum we sliced off
    # the NMEA sentence

    res = 0
    for c in chksumdata:
        # XOR'ing value of csum against the next char in line
        # and storing the new XOR value in csum
        csum ^= ord(c)
    res = hex(csum)[hex(csum).find("x")+1:len(hex(csum))]
    print(res)


    # Do we have a validated sentence?
    if hex(csum) == hex(int(cksum, 16)):
        print("ok!")
    else:
        print("cksum incorrect")


chksum_nmea('$GPHDG,65.0,1,,0.5,T*23')