# Extended Berkeley Packet Filter (eBPF) 소개

## 개요
eBPF(Extended Berkeley Packet Filter)는 원래 네트워크 패킷 필터링을 위해 설계된 BPF(Berkeley Packet Filter)를 확장한 기술로, 리눅스 커널 내에서 안전하고 효율적으로 코드를 실행할 수 있게 해줍니다. eBPF는 네트워크 패킷 처리뿐만 아니라, 성능 모니터링, 보안 강화, 트레이싱 등 다양한 용도로 활용됩니다.

## 역사 및 배경
- **Berkeley Packet Filter(BPF):** 1992년에 개발된 BPF는 네트워크 패킷 캡처와 필터링을 위한 기술로, tcpdump와 같은 도구에서 사용되었습니다.
- **Extended BPF(eBPF):** 2014년 리눅스 커널 3.18에서 도입된 eBPF는 BPF의 기능을 확장하여 네트워크뿐만 아니라 시스템 전반에 걸쳐 다양한 용도로 사용될 수 있도록 설계되었습니다.

## 주요 특징
### 1. 안전성
eBPF 프로그램은 커널 내에서 실행되기 전에 검증기를 통과하여 안전성을 보장합니다. 이 검증기는 무한 루프 방지, 메모리 안전성, 권한 제어 등을 검사합니다.

### 2. 성능
eBPF는 JIT(Just-In-Time) 컴파일러를 사용하여 바이트 코드를 네이티브 기계 코드로 변환함으로써 높은 성능을 제공합니다. 이는 기존 커널 모듈 방식보다 더 빠르고 효율적입니다.

### 3. 유연성
eBPF는 다양한 후크(hook)를 제공하여 네트워크 패킷 필터링, 트레이싱, 모니터링, 보안 정책 적용 등 다양한 작업을 수행할 수 있습니다.

## 사용 사례
### 1. 네트워크 패킷 필터링
eBPF는 고성능 패킷 필터링을 제공하여 방화벽, 로드 밸런싱, DDoS 방어 등에 사용됩니다. 예를 들어, Cilium은 eBPF를 사용하여 네트워크 보안을 강화하는 오픈 소스 프로젝트입니다.

### 2. 성능 모니터링
eBPF는 시스템 성능 모니터링 도구로 널리 사용됩니다. bcc(BPF Compiler Collection)와 같은 도구는 eBPF를 활용하여 다양한 시스템 메트릭을 수집하고 분석합니다.

### 3. 보안
eBPF는 런타임 보안 검사를 수행하고, 악성 활동을 실시간으로 감지하여 보안을 강화합니다. Tracee와 같은 도구는 eBPF를 사용하여 컨테이너 보안을 제공합니다.

## eBPF 프로그램 작성 및 실행
### 1. 프로그램 작성
eBPF 프로그램은 일반적으로 C 언어로 작성되며, clang을 사용하여 BPF 바이트 코드로 컴파일됩니다.

```c
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

SEC("xdp")
int xdp_prog(struct xdp_md *ctx) {
    // 패킷을 드롭
    return XDP_DROP;
}

char _license[] SEC("license") = "GPL";
```

### 2. 프로그램 로드 및 실행
컴파일된 eBPF 프로그램은 `iproute2`, `libbpf`, `bpftool` 등의 도구를 사용하여 커널에 로드되고 실행됩니다.

```sh
clang -O2 -target bpf -c xdp_prog.c -o xdp_prog.o
ip link set dev eth0 xdp obj xdp_prog.o sec xdp
```

## 결론
eBPF는 리눅스 커널에서 사용자 정의 코드를 안전하고 효율적으로 실행할 수 있게 해주는 강력한 도구입니다. 네트워크 관리, 성능 모니터링, 보안 강화 등 다양한 분야에서 활용될 수 있으며, 리눅스 생태계에서 점점 더 중요한 역할을 하고 있습니다.

## 참고 자료
- [eBPF 프로젝트 홈페이지](https://ebpf.io)
- [BCC(BPF Compiler Collection) GitHub](https://github.com/iovisor/bcc)
- [Cilium GitHub](https://github.com/cilium/cilium)

---

이 문서에서는 eBPF의 개요, 역사, 주요 특징, 사용 사례, 프로그램 작성 및 실행 방법에 대해 설명했습니다. eBPF는 리눅스 커널 내에서 다양한 작업을 수행할 수 있는 유연하고 강력한 기술로, 향후에도 그 중요성이 증가할 것으로 예상됩니다.