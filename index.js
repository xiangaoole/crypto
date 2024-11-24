import bs58 from "bs58";
import { createHash } from 'crypto';


const base58Check = (hex) => {
  const hash = createHash('sha256').update(Buffer.from(hex, 'hex')).digest();
  const doubleHash = createHash('sha256').update(hash).digest();
  const checksum = doubleHash.slice(0, 4);
  return bs58.encode(Buffer.concat([Buffer.from(hex, 'hex'), checksum]));
}

const hexString = "1e99423a4ed27608a15a2616a2b0e9e52ced330ac530edcc32c8ffc6a526aedd";
const wif = base58Check("80" + hexString);
const wifCompressed = base58Check("80" + hexString + "01");
console.log(wif);
console.log(wifCompressed);
