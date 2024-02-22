# AES

`AES`(***Advanced Encryption Standard***)는 `대칭 키 알고리즘` 중 하나로, 데이터를 암호화하고 복호화하기 위해 사용됩니다. 256비트 수준의 AES는 AES 알고리즘에서 `키의 길이가 256비트인 경우`를 의미합니다. 이것은 AES에서 사용할 수 있는 키 길이 중 가장 긴 것입니다.

<br>

AES는 블록 암호화 방식 중 하나로, `고정된 크기의 블록`(128비트)을 `입력`으로 받아 `출력 블록으로 변환하는 과정을 반복`함으로써 데이터를 암호화합니다. 간단히 말해, AES는 입력 블록을 연속적으로 변형시키는 라운드라는 단계를 거쳐 암호화를 수행합니다.

256비트 수준의 AES에서는 키 길이가 256비트이므로, 이 키를 사용하여 암호화 및 복호화를 수행합니다. 암호화 및 복호화 과정에서 사용되는 주요 구성 요소로는 다음이 있습니다.

1. SubBytes: 16바이트의 입력 블록의 각 바이트를 S-Box를 통해 다른 바이트로 대체합니다.
2. ShiftRows: 16바이트의 입력 블록을 행 단위로 순환 이동시킵니다.
3. MixColumns: 각 열을 선형 변환합니다.
4. AddRoundKey: 현재 라운드의 라운드 키를 입력 블록에 적용합니다.

이러한 단계를 여러 번 반복하여 최종적으로 `암호문`(암호화된 메시지)을 생성합니다. 복호화 과정에서는 각 단계를 역순으로 적용하여 원본 메시지를 복원합니다.

`256비트 수준의 AES는 보안 강도가 높은 암호화를 제공`합니다. 키의 길이가 길어짐에 따라 암호화의 강도가 강화되므로, 더 안전한 데이터 보호를 위해 사용될 수 있습니다.
