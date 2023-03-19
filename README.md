# **XRPL-Solvency - Local ring proof generation and verification environment**

This executable developed in python during the **PBWS 2023 hackathon** is the local environnement to create ring signature for XRPL solvency. 

This app allows you to generate your creditworthiness proof based on ring signatures directly in your local environment. Each time a proof is created, an SBT (Soul Bound Token) is minted and the data are stored on IPFS. 
It also allows you to verify the signatures, by retrieving them directly from our web-app.

## **What are ring-signature** 💍
Ring signatures are a type of digital signature that allows a user to sign a message on behalf of a group without revealing which specific member signed it. The signature is created using a group of possible signers, or a "ring," and any one of the members in the ring can create the signature without revealing their identity. This makes it a useful tool for maintaining privacy in various applications, such as cryptocurrencies, whistleblowing, and anonymous messaging.
In our solution we use ring signature to give you access to proof of solvency while maintaining your privacy.

## **Configuration** 📝

1. Go on our [website](https://web-app-virid-theta.vercel.app).
2. On the generate Proof page click on download.
3. Open ring_proof.exe and pass the arguments for your signature.
4. Your done, you have minted your SBT !!!

1. Go on our [website](https://web-app-virid-theta.vercel.app).
2. On the verify Proof page click on download.
3. Open ring_proof_verify.exe and pass the arguments for the proof you want to verify.
4. Your done, you have verify a proof !!!
