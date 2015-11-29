import sys
import subprocess



import easygui
result = easygui.multenterbox("Enter your name", "Name query", ["Filename","whateva"])
print result[1]
    
inmagicxml = sys.argv[1] + '.xml'
updated = inmagicxml + 'updated.xml'
with open(inmagicxml, "w+") as fo:

    fo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fo.write('<revtmd xmlns:revtmd="http://nwtssite.nwts.nara/schema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://nwtssite.nwts.nara/schema/  http://www.archives.gov/preservation/products/reVTMD.xsd">\n')
    fo.write('<revtmd:reVTMD>\n')
    fo.write('<revtmd:object>\n')
    fo.write('<revtmd:filename/>\n')
    fo.write('<revtmd:organization>\n')
    fo.write('<revtmd:organization_main>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('</revtmd:organization_main>\n')
    fo.write('<revtmd:organization_division>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('</revtmd:organization_division>\n')
    fo.write('</revtmd:organization>\n')
    fo.write('<!-- Use for custodian of the content item -->\n')
    fo.write('<revtmd:organization>\n')
    fo.write('<revtmd:organization_main>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:role_note/>\n')
    fo.write('</revtmd:organization_main>\n')
    fo.write('</revtmd:organization>\n')
    fo.write('<revtmd:identifier/>\n')
    fo.write('<revtmd:mimetype/>\n')
    fo.write('<revtmd:checksum algorithm="" dateTime=""/>\n')
    fo.write('<!-- Checksum as generated immediately after the digitization process. -->\n')
    fo.write('<revtmd:use/>\n')
    fo.write('<revtmd:captureHistory>\n')
    fo.write('<revtmd:digitizationDate/>\n')
    fo.write('<revtmd:digitizationEngineer/>\n')
    fo.write('<revtmd:digitizationEngineer/>\n')
    fo.write('<revtmd:preparationActions/>\n')
    fo.write('<revtmd:preparationActions/>\n')
    fo.write('<!-- Here you list the tools used to create the object being described in this record.\n')
    fo.write('For example, if you are creating a record for a low-quality viewing copy, you would describe\n')
    fo.write('all of the tools used to get from the higher quality preservation copy to the viewing copy. -->\n')
    fo.write('<revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:description/>\n')
    fo.write('<revtmd:manufacturer/>\n')
    fo.write('<revtmd:modelName/>\n')
    fo.write('<revtmd:serialNumber/>\n')
    fo.write('<revtmd:signal/>\n')
    fo.write('<revtmd:settings/>\n')
    fo.write('</revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:description/>\n')
    fo.write('<revtmd:manufacturer/>\n')
    fo.write('<revtmd:modelName/>\n')
    fo.write('<revtmd:serialNumber/>\n')
    fo.write('<revtmd:signal/>\n')
    fo.write('<revtmd:settings/>\n')
    fo.write('</revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:description/>\n')
    fo.write('<revtmd:manufacturer/>\n')
    fo.write('<revtmd:modelName/>\n')
    fo.write('<revtmd:serialNumber/>\n')
    fo.write('<revtmd:signal/>\n')
    fo.write('<revtmd:settings/>\n')
    fo.write('</revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:description/>\n')
    fo.write('<revtmd:manufacturer/>\n')
    fo.write('<revtmd:modelName/>\n')
    fo.write('<revtmd:serialNumber/>\n')
    fo.write('<revtmd:signal/>\n')
    fo.write('<revtmd:settings/>\n')
    fo.write('</revtmd:codingProcessHistory>\n')
    fo.write('</revtmd:captureHistory>\n')
    fo.write('</revtmd:object>\n')
    fo.write('</revtmd:reVTMD>\n')
    fo.write('</revtmd>\n')
    
    

subprocess.call(['xml', 'ed', '--inplace', '-N', 'x=http://nwtssite.nwts.nara/schema/', '-u', '//revtmd:filename', '-v', result[1], inmagicxml])


subprocess.call(['xml', 'ed','--inplace', '-N', 'x=http://nwtssite.nwts.nara/schema/', '-u', '//revtmd:identifier', '-v', result[0], inmagicxml])


subprocess.call(['xml', 'ed','--inplace', '-N', 'x=http://nwtssite.nwts.nara/schema/', '-u', '//revtmd:digitizationEngineer[1]', '-v', "Kieran O'Leary", inmagicxml])

