# :video_game: Share My Hobby
동네기반 취미공유 서비스 - **Share My Hobby**

<p align="center">
  <a href="https://www.freepik.com/vectors/person">
    <img src="https://user-images.githubusercontent.com/21170717/121205986-0f84e180-c8b3-11eb-9573-3e06063fe6cf.jpg"  width="600" height="400">
  </a>
</p>

## :bulb: 서비스 및 프로젝트 소개
**`Share My Hobby`** 는 이웃들과 함께 취미를 공유할 수 있는 커뮤니티 서비스 입니다. 사용자들은 온라인 상에서 자신이 살고 있는 동네를 기반으로 이웃들과 관심있는 취미에 대한 이야기를 나누고, 정보를 교류하고, 취미를 전파하기 위한 자신만의 클래스를 개설할 수도 있습니다. 본 프로젝트는 **`Share My Hobby`** 의 서버 개발을 하며 만났던 다양한 문제들과 그런 문제들을 해결하기 위해 고민했던 내용들, 그리고 실제 구현 코드들을 담고 있습니다.  
항상 다음과 같은 질문을 던지며 프로젝트를 진행하고 있습니다.

 1. 이 코드들은 충분히 확장에 용이한가?
 2. 이 아키텍처는 대용량의 트래픽에도 안정적인가?  
 3. 사용성을 더욱 개선시킬 수는 없을까?

아직 구현해야할 기능과 해결해야할 이슈들이 많이 남아있지만, 어떤 상황에서도 견고한 서비스를 만들기 위해 꾸준히 개선해나갈 예정입니다.

## :mag: 서비스 기능
**`Share My Hobby`** 에는 크게 다음과 같은 기능들이 있습니다. 더 자세한 내용들은 [이곳](https://github.com/f-lab-edu/share-my-hobby/wiki/2.-%EA%B8%B0%EB%8A%A5-%EC%A0%95%EC%9D%98)을 참고해 주세요.

- 자신과 관심 취미가 맞는 이웃들과 함께 자유롭게 이야기를 나눌 수 있습니다.
- 자신의 취미를 전수하고 싶은 분들은 자신만의 취미 클래스를 개설할 수 있습니다.
- 우리 동네에서 즐길 수 있는 취미와 관련된 정보들을 제공받을 수 있습니다.(예정)

## :rocket: 프로젝트 목표
서비스의 기능을 구현하는 것 자체도 중요하지만, **어떤 과정을 통해 어떻게 구현했는지**가 그 이상으로 중요하다고 생각합니다. 예를 들어, 실무에서는 개인이 아닌 팀 단위로 개발을 진행하기 때문에 합의된 코딩 스타일과 개발 프로세스를 유지해야 하고 효율적인 협업 방식을 고려해야합니다. 또 실무에서의 서비스 규모는 훨씬 크고 복잡하기 때문에 유지보수성 고려하여 일정 좋은 코드 퀄리티와 유연한 설계를 유지해야 합니다.  
따라서 **`Share My Hobby`** 개발 프로젝트에서는 아래와 같은 목표들을 세운 후, 팀 단위로 실제 운영 중인 서비스를 개발하는 상황에서 어떻게 이와 같은 목표를 달성할 수 있을지 고민하며 개발을 진행하고 있습니다.
1. **유연한 설계와 확장성 높은 코드로 유지보수성을 높이자**
    - 여기저기 중복되는 코드들, 기능을 수정하고 추가할 때 마다 불필요한 수정을 필요로 하는 상황들을 최소화하고 유지보수성을 높이기 위해 노력합니다.
    - 이를 위해 SOLID 원칙과 디자인 패턴에 대한 이해를 바탕으로 객체지향의 장점을 최대한 활용하는 코드를 작성합니다.

2. **대용량 트래픽을 고려하여 아키텍처를 구성하자**
    - 서비스가 빠르게 성장함에 따라 함께 빠르게 증가하는 트래픽에도 견딜 수 있는 아키텍처를 설계하기 위해 노력합니다.
    - 아키텍처를 구성하는 다양한 방법들 간의 trade-off를 분석하고 분석한 내용을 바탕으로 설계를 진행합니다.

3. **테스트 코드를 통해 개발한 코드의 신뢰를 높이자**
    - 안정적인 서비스를 개발하기 위해 테스트 코드는 필수입니다. 꼼꼼히 작성된 테스트 코드들은 개발한 코드의 올바른 동작을 보장해주며 이를 통해 다른 팀원들에게도 신뢰를 줄 수 있습니다. 또 잘 작성된 테스트 코드 목록은 전체적인 서비스를 파악할 수 있는 하나의 명세서 역할을 하기도 합니다.
    - 따라서 기능을 수정/추가할 때마다 반드시 테스트 코드를 작성하되 빠른 테스트를 통한 효율적인 개발 사이클을 유지하기 위해 테스트 스텁(stub)을 활용하여 고립된 단위 테스트 코드를 작성합니다.

4. **문서화를 통해 협업 효율성을 높이자**
    - 프론트엔드-백엔드 팀이 협업하는 환경에서 요청과 응답 방식에 대해 잘 정리된 API 문서는 원활한 커뮤니케이션을 도와주는 좋은 자료가 됩니다. 뿐만 아니라 외부의 사용자가 우리가 개발한 API를 호출하기 위해서도 API 문서는 필수적입니다. 
    - 하지만 개발을 진행하며 API 문서를 함께 직접 작성하는 것은 비효율적이기 때문에 Spring RestDocs와 같은 툴을 활용하여 문서 작업을 자동화할 수 있는 방법을 고민합니다.

5. **CI/CD를 구축하여 개발 프로세스의 효율성을 높이자**
    - 다수의 개발자가 하나의 서비스를 개발해나가는 환경에서는 각자의 코드를 머지하고 충돌을 해결하고 테스트하고 빌드, 배포하는 과정에도 많은 리소스가 소요됩니다. 이러한 문제를 해결하기 위한 방법으로 CI/CD를 직접 구축하여 애자일한 개발 프로세스를 실현하기 위해 노력합니다.

6. **성능 테스트를 통한 성능을 개선하자**
    - 실제 서비스 환경에서 트래픽이 몰리는 경우 예상치 못한 문제들이 발생할 수 있기 때문에 성능 테스트 역시 반드시 병행되어야 합니다. 성능 테스트를 통해 병목 지점을 개선하고 컴퓨팅 자원을 더 효율적을 활용할 수 있는 방안들을 고민하여 성능을 향상시키기 위해 노력합니다.
    - nGrinder와 Pinpoint와 같은 툴을 이용해 높은 트래픽을 발생시키고 성능을 모니터링하여 개선점을 찾아냅니다.
    

## :wrench: 사용 기술 스택
- Python 1.8
- scikitLearn
- MySQL 8.0
- Django
- Pandas
- Matlib


## :robot: 프로젝트 아키텍처
![system_architecture](https://user-images.githubusercontent.com/21170717/121297109-c7a2a080-c92c-11eb-80e2-233970ec701b.png)

## :heavy_exclamation_mark: 이슈 정리
- Wiki의 [이슈 해결](https://github.com/f-lab-edu/share-my-hobby/wiki/5.-%EC%9D%B4%EC%8A%88-%ED%95%B4%EA%B2%B0)을 참고해 주세요.

## :floppy_disk: ER Diagram
- 지속적으로 업데이트 중입니다.

![erd](https://user-images.githubusercontent.com/21170717/121324479-bd43cf00-c94b-11eb-9990-b19bd42c6c45.png)