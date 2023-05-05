import random
from OpenSSL import crypto, SSL
import boto3


def createImportCert():
    # step-01-Create Certificate Authority (CA)
    #############################################

    # create root key
    root_key = crypto.PKey()
    root_key.generate_key(crypto.TYPE_RSA, 2048)

    # create root certificate-subject
    ca_cert = crypto.X509()
    ca_cert.set_version(2)
    ca_cert.set_serial_number(random.randrange(1000))
    ca_subj = ca_cert.get_subject()
    ca_subj.C = "NL"
    ca_subj.ST = "eindhoven"
    ca_subj.L = "eindhoven"
    ca_subj.O = "TGO"
    ca_subj.OU = "TGOU"
    ca_subj.CN = "eu-central-1.elb.amazonaws.com"

    # create root certificate-issuer.Both subject and issuer are same here
    ca_cert.set_issuer(ca_subj)
    ca_cert.set_pubkey(root_key)

    # signed with the root key itself
    ca_cert.sign(root_key, 'sha256')

    # validity in seconds 
    ca_cert.gmtime_adj_notBefore(0)
    ca_cert.gmtime_adj_notAfter(10*365*24*60*60)

    # dumping the certificate 
    ca_cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, ca_cert).decode('utf-8')

    # step-02-Create Self-Signed Certificate
    #############################################

    # generate a key to be used by the client
    client_key = crypto.PKey()
    client_key.generate_key(crypto.TYPE_RSA, 2048)

    # create a client certificate
    client_cert = crypto.X509()
    client_cert.set_version(2)
    client_cert.set_serial_number(random.randrange(10000))
    client_subj = client_cert.get_subject()
    client_subj.C = "NL"
    client_subj.ST = "eindhoven"
    client_subj.L = "eindhoven"
    client_subj.O = "MySite"
    client_subj.OU = "MyOU"
    client_subj.CN = "eu-central-1.elb.amazonaws.com"

    # create  certificate-issuer.The issuer is the CA created as above
    client_cert.set_issuer(ca_subj)

    # set the public key for the client cert
    client_cert.set_pubkey(client_key)

    # define the validity of the certificate
    client_cert.gmtime_adj_notBefore(0)
    client_cert.gmtime_adj_notAfter(2*365*24*60*60)

    # sign the client certificate with the root key of CA
    client_cert.sign(root_key, 'sha256')

    # dumping the certificate
    certificate_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, client_cert).decode('utf-8')
    private_key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, client_key).decode('utf-8')

    # creating the files for debugging purpose
    # with open('./certs/certificate.crt', 'wt') as f:
    #     f.write(certificate_pem)

    # with open('./certs/privateKey.key', 'wt') as k:
    #     k.write(private_key_pem)

    # with open('./certs/ca_cert.crt', 'wt') as c:
    #     c.write(ca_cert_pem)

    response_import = acm_client.import_certificate(Certificate=certificate_pem, 
        PrivateKey=private_key_pem,
        CertificateChain=ca_cert_pem)
    arn_cert = response_import['CertificateArn'] 
    return arn_cert


# calls the list_certificates to check if certificate exists
acm_client = boto3.client('acm') 
response_listCerts = acm_client.list_certificates(CertificateStatuses=['ISSUED'] )
cert_summaryList = response_listCerts['CertificateSummaryList']

# if there are no existing certs, call the function to create one and upload it to the account and then get its arn
# else use the existing one
if len(cert_summaryList)==0:
    cert_arn = createImportCert()
else:
    cert_arn = response_listCerts ['CertificateSummaryList'] [0]['CertificateArn']

# debugging purpose
# print ("cert arn from the createImport file is  ", cert_arn) 

