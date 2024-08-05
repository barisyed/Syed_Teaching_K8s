
# Get the current date and time
$timestamp = Get-Date -Format "yyyyMMdd_HHmm"

# Set the file name
$fileName = "date"

# Create the new file name with the timestamp
$newFileName = "{0}_{1}" -f $timestamp, $fileName

# Rename the file
Rename-Item -Path $fileName -NewName $newFileName

cd \
cd "C:\Program Files\Siemens\Capital2408_1202\bin"

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2020_$newFileName.csv -NoTypeInformation

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2408.csv -NoTypeInformation

echo "Capital2408 Digital Testing Report Generated"

cd \
cd C:\MentorGraphics\Capital2020.1\bin

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2020_$newFileName.csv -NoTypeInformation

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2020.csv -NoTypeInformation

echo "Capital2020 Digital Testing Report Generated"

cd \
cd C:\MentorGraphics\Capital2021.1\bin



Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2021_$newFileName.csv -NoTypeInformation

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2021.csv -NoTypeInformation

echo "Capital2021 Digital Testing Report Generated"


cd \
cd C:\MentorGraphics\Capital2207\bin

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2207_$newFileName.csv -NoTypeInformation

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2207.csv -NoTypeInformation

echo "Capital2207 Digital Testing Report Generated"

cd \
cd "C:\MentorGraphics\capital_2308_996\bin"

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2308_$newFileName.csv -NoTypeInformation

Get-ChildItem *.exe | Get-AuthenticodeSignature |` Select-object -Property Path, Status,StatusMessage,SignatureType,` @{Name='Valid Date From';Expression={($_.SignerCertificate.NotBefore)}}, ` @{Name='Expiry Date';Expression={($_.SignerCertificate.NotAfter)}}, ` @{Name='CertificateIssuer';Expression={($_.SignerCertificate.Issuer)}}, ` @{Name='SerialNumber';Expression={($_.SignerCertificate.SerialNumber)}} | Export-Csv C:\apps\Digital_testing_capital_2308.csv -NoTypeInformation

echo "Capital2308 Digital Testing Report Generated"

python C:\Users\itcqa2\Documents\digitalSignaturePythonfiles\DigitalCertificateValidation.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "To view validated Reports go to the path c:\apps"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd \
cd C:\apps


$sourceFolder = Get-Location
$destinationFolder = "C:\Siemens\Digital_Logs"

# Create the destination folder if it doesn't exist
if (-not (Test-Path -Path $destinationFolder)) {
    New-Item -ItemType Directory -Path $destinationFolder | Out-Null
}

# Copy files from the source folder to the destination folder
Copy-Item -Path "$sourceFolder\*" -Destination $destinationFolder -Force

echo "All logs backup available at C:\Siemens\Digital_Logs"

PowerShell -NoExit
