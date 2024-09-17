#Make a C+ or c++ program that encrypts a file using a AES encryption algorithm.
#The program should take the file name as an argument and encrypt the file.
#The program should also take a password as an argument and use the password to encrypt the file.
#The program should output the encrypted file to a file with the same name as the input file but with a .enc extension.
#The program should also output the key used to encrypt the file to a file with the same name as the input file but with a .key extension.

#include <iostream>
#include <fstream>
#include <string>
#include <openssl/aes.h>
#include <openssl/rand.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/conf.h>
#include <openssl/err.h>
#include <openssl/evp.h>

using namespace std;

void handleErrors(void)
{
    ERR_print_errors_fp(stderr);
    abort();
}

int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
            unsigned char *iv, unsigned char *ciphertext)
{
    EVP_CIPHER_CTX *ctx;

    int len;

    int ciphertext_len;

    if (!(ctx = EVP_CIPHER_CTX_new()))
        handleErrors();

    if (1 != EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv))
        handleErrors();

    if (1 != EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len))
        handleErrors();
    ciphertext_len = len;

    if (1 != EVP_EncryptFinal_ex(ctx, ciphertext + len, &len))
        handleErrors();
    ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);

    return ciphertext_len;
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        cout << "Usage: " << argv[0] << " <file> <password>" << endl;
        return 1;
    }

    string file = argv[1];
    string password = argv[2];

    ifstream in(file, ios::binary);
    if (!in)
    {
        cout << "Error opening file: " << file << endl;
        return 1;
    }

    in.seekg(0, ios::end);
    int plaintext_len = in.tellg();
    in.seekg(0, ios::beg);

    unsigned char *plaintext = new unsigned char[plaintext_len];
    in.read((char *)plaintext, plaintext_len);
    in.close();

    unsigned char key[32];
    unsigned char iv[16];

    RAND_bytes(key, 32);
    RAND_bytes(iv, 16);

    unsigned char *ciphertext = new unsigned char[plaintext_len + AES_BLOCK_SIZE];

    int ciphertext_len = encrypt(plaintext, plaintext_len, key, iv, ciphertext);

    string enc_file = file + ".enc";
    ofstream out(enc_file, ios::binary);
    out.write((char *)ciphertext, ciphertext_len);
    out.close();

    string key_file = file + ".key";
    out.open(key_file, ios::binary);
    out.write((char *)key, 32);
    out.close();

    delete[] plaintext;
    delete[] ciphertext;

    return 0;
}
