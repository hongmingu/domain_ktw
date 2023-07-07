import React from 'react';
import Link from 'next/link';
import { getPosts } from '../utils/mdx-utils';

import Footer from '../components/Footer';
import Header from '../components/Header';
import Layout, { GradientBackground } from '../components/Layout';
import ArrowIcon from '../components/ArrowIcon';
import { getGlobalData } from '../utils/global-data';
import SEO from '../components/SEO';

const Custom404 = () => (
  <>
    <Layout>
      <SEO title="한국 스포츠 대표 정보 블로그" description="다양한 스포츠 소식이 한 가득" />
      <Header name="한국팀승리" />
      <main className="w-full">
        <h1>스포츠 티켓 예매 방법</h1>
        <h2>1. 경기 일정 파악</h2>
        <p>먼저, 관람하고 싶은 경기의 일정을 파악해야 합니다...</p>
        <h2>2. 예매 사이트 알아보기</h2>
        <p>
          예매는 대개 공식 웹사이트 또는 다른 온라인 티켓 판매 사이트를 통해
          이루어집니다...
        </p>
        <h2>3. 티켓 가격과 좌석 확인</h2>
        <p>티켓 가격은 좌석 위치, 경기 중요도, 팀 등에 따라 다릅니다...</p>
        <h2>4. 예매 시작 시간 확인</h2>
        <p>
          일반적으로 티켓 예매는 경기 일정이 공개되는 시점부터 시작됩니다...
        </p>
        <h2>5. 티켓 구매</h2>
        <p>
          티켓을 구매하려면 일반적으로 회원 가입이 필요하며, 티켓 가격을 온라인
          결제해야 합니다...
        </p>
        <h2>6. 티켓 확인</h2>
        <p>
          티켓을 받은 후에는 날짜, 시간, 좌석 번호 등이 정확한지 확인해야
          합니다...
        </p>
        <h2>7. 경기장 방문</h2>
        <p>
          경기 당일에는 티켓과 신분증을 지참하고, 경기 시작 시간 이전에 경기장에
          도착해야 합니다...
        </p>
        <p>
          이상으로 스포츠 티켓 예매 방법에 대해 설명하였습니다. 올바른 절차를
          따르면, 관객은 스포츠 경기를 안전하고 편안하게 즐길 수 있습니다.
        </p>
        <h2>예매할 수 있는 사이트 목록</h2>
        <ul>
          <li>
            <a
              href="https://www.playkfa.com/"
              target="_blank"
              rel="noopener noreferrer"
            >
              한국축구협회(KFA)
            </a>
          </li>
          <li>
            <a
              href="https://ticket.interpark.com/"
              target="_blank"
              rel="noopener noreferrer"
            >
              인터파크 티켓
            </a>
          </li>
          <li>
            <a
              href="https://www.ticketlink.co.kr/home"
              target="_blank"
              rel="noopener noreferrer"
            >
              티켓링크
            </a>
          </li>
        </ul>
        <p>
          <a
            href="https://koreateam.win/index.html"
            target="_blank"
            rel="noopener noreferrer"
          >
            더 자세한 스포츠 정보 보러가기
          </a>
        </p>
        <ul className="w-full">
          {posts.map((post) => (
            <li
              key={post.filePath}
              className="md:first:rounded-t-lg md:last:rounded-b-lg backdrop-blur-lg bg-white dark:bg-black dark:bg-opacity-30 bg-opacity-10 hover:bg-opacity-20 dark:hover:bg-opacity-50 transition border border-gray-800 dark:border-white border-opacity-10 dark:border-opacity-10 border-b-0 last:border-b hover:border-b hovered-sibling:border-t-0"
            >
              <Link
                as={`/posts/${post.filePath.replace(/\.mdx?$/, '')}`}
                href={`/posts/[slug]`}
              >
                <a className="py-6 lg:py-10 px-6 lg:px-16 block focus:outline-none focus:ring-4">
                  {post.data.date && (
                    <p className="uppercase mb-3 font-bold opacity-60">
                      {post.data.date}
                    </p>
                  )}
                  <h2 className="text-2xl md:text-3xl">{post.data.title}</h2>
                  {post.data.description && (
                    <p className="mt-3 text-lg opacity-60">
                      {post.data.description}
                    </p>
                  )}
                  <ArrowIcon className="mt-4" />
                </a>
              </Link>
            </li>
          ))}
        </ul>
      </main>
      <Footer copyrightText={globalData.footerText} />
      <GradientBackground
        variant="large"
        className="fixed top-20 opacity-40 dark:opacity-60"
      />
      <GradientBackground
        variant="small"
        className="absolute bottom-0 opacity-20 dark:opacity-10"
      />
    </Layout>
  </>
);

export default Custom404;