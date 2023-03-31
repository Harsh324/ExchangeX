import Kyc.kyc.kyc_functions as Kyc

## using the kyc module

name = "harsh"
email = "admin@gmail.com"
address = ";lsgj kebs gzdzm s,md"
dob = "2002-12-28"
docName = "aadhar"
docNumber = "23589387493456"
kycObj = Kyc.Kyc(name, email, address, dob, docName, docNumber).addToDatabase()
