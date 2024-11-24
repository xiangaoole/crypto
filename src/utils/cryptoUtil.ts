import bs58 from "bs58";
import { createHash } from "crypto";

export const base58Check = (hex: string) => {
  const hash = createHash("sha256").update(Buffer.from(hex, "hex")).digest();
  const doubleHash = createHash("sha256").update(hash).digest();
  const checksum = doubleHash.slice(0, 4);
  return bs58.encode(Buffer.concat([Buffer.from(hex, "hex"), checksum]));
};
