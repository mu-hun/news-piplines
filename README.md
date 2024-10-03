# 세계 뉴스, 내 손안에: 외신 기사 종합 수집 파이프라인

> 크리에이티브 커먼즈 위키 문서 중에 [저널리즘 문서](https://wiki.creativecommons.org/wiki/Journalism) 참고

크리에이티브 커먼즈 조항 중 ["저작자 표시" 및 "변경 허용" CC-BY 라이선스](https://creativecommons.org/licenses/by/4.0/deed.ko)를 명시한 Wikinews와 Global Voices를 선택하게 되었습니다.

대부분의 저널이 자사의 콘텐츠에 대해 2차 사용을 제한해 두고 있어 콘텐츠 수집의 폭이 넓지 않아 이 두 저널을 선택하게 되었습니다.

## Wikinews RSS feed

endpoints: `https://{en,jp}.wikinews.org/w/index.php`

## example: Latest news

```json
{
  "title": "Special:NewsFeed",
  "feed": "atom",
  "categories": "South_America",
  "notcategories": "No publish|Archived|AutoArchived|disputed",
  "namespace": "0",
  "count": "30",
  "ordermethod": "categoryadd",
  "stablepages": "only"
}
```

- `categories` 속성에 [`South_America`](https://en.wikinews.org/wiki/Category:South_America), [`Crime_and_law`](https://en.wikinews.org/wiki/Category:Crime_and_law) 등 위키 카테고리를 `|` 를 구분자로 넣어 쿼리하면 됩니다. 예) `South_America|Crime_and_law`
- `count`: 가져올 기사 갯수
- `hourcount`: 지난 몇시간 동안의 기사를 가져올지

## Global Voices RSS feed

https://globalvoices.org/feeds/ TODO

## 자동화

![cron](https://github.com/mu-hun/news-piplines/actions/workflows/cron.yml/badge.svg)

매일 9시마다 [cron workflow](https://github.com/mu-hun/news-piplines/actions/workflows/cron.yml)를 통해 데이터베이스에 외신 기사를 업데이트하고 있습니다.
