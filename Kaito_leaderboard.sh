
#!/usr/bin/env bash
# Save as gomtu_fetch.sh, then: chmod +x gomtu_fetch.sh && ./gomtu_fetch.sh > gomtu_results.ndjson
set -euo pipefail
usernames=(theganfam choog_sol 0xCryptoUni AL__0077 HottieBabeGem VIP8888883 lenioneall web3Lyra JiuHuangKOL BitcoinZac Louis__Fok eliasdejesusmq 0xjayn3 hassanyehiaa NoraXBT Skuullls Trentowtf evans1vn ken_w3b3 BeiDao_98 iamyoungjohnn Web3Pikachu iiamchucky CryptoLycus dakuan_x FeratMDS Jaxon0x 0xDecision DegenShoots CandyDAO_leaf 0xGiwax Skinny19999 custommade_ng Cryptohitmaniac duoduo95920292 omnicryptx FerreWeb3 killstoryyy InfluencerDee xmayeth ShepengWeb3 sunominq wangy112375 jiao_newlife blueerush taozi0929 ShuvoWeb3 egyptk6 0xnewren bigray0x 0xYi666 Husaink0404 Joestar_sann itsmepris0ner officialabdulak timbro_bro Beatriz_Ape Defi_Scribbler bynlalala ajey_eth David__GMI Keeperssd 0xadriandefi gushanjishui SaulWgmi VisionaryLorien xCryptoAlucard TweetByWale defimhamad maziibe_ Ciciyingying WinxWeb3 nft_pilot SharkyWeb3 0x8Gluck Jerrytee08 Alifa__ 0x_Fenda lordkolie afanda1988 SebyCore KakashiAirdrops itsyourabdul Adellbah Anastasis_Delta HeinrichDefi DuMing521 0x0Nova jexybtc youyou8178 FoamSol ArunimaGanguly2 Doflam656 Web3heinu degen_sensei18 faizantariq26 Benjieming1Q84 KingWilliamDefi wuyou88818 parcifap_defi)
for u in "${{usernames[@]}}"; do
    url=" " # e.g. https://gomtu.xyz/api/yap/open?username=${{u}}
    resp=$(curl -sS "$url") || resp="{{}}"
    printf '{{"username":"%s","response":%s}}\n' "$u" "$resp"
    sleep 0.3
done
