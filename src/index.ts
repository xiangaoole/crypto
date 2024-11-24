import { base58Check } from "./utils/cryptoUtil";

const hexString = "1e99423a4ed27608a15a2616a2b0e9e52ced330ac530edcc32c8ffc6a526aedd";
const wif = base58Check("80" + hexString);
const wifCompressed = base58Check("80" + hexString + "01");
console.log(wif);
console.log(wifCompressed);
