import Footer from "./Footer"
import Navbar from "./Navbar"
import Head from 'next/head'

interface Props {
    lastThreePosts: Array<object>,
    cv: Array<object>,
    postMetas: Array<object>,
    pageMetas: Array<any>,
    lastProject: any,
    children: any,
    title: string
}

const Layout = ({ lastThreePosts, cv, lastProject, title, postMetas, pageMetas, children }: Props) => {

    return (
        <div>
            <Head>
                <title>{`${title.length === 0 ? (pageMetas ? pageMetas[0].page.title : "EILYA AMIN") : title}`}</title>
                <link rel="icon" href="/favicon.ico" />
                {postMetas.map((meta: any) => {
                    return (
                        <meta name={`${meta.name}`} content={`${meta.content}`} />
                    )
                })}
                {pageMetas && pageMetas.map((meta: any, index: number) => {
                    return (
                        <meta key={index} name={`${meta.name}`} content={`${meta.content}`} />
                    )
                })}
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            </Head>

            <Navbar />
            {children}
            <Footer lastThreePosts={lastThreePosts} lastProject={lastProject} cv={cv} />
        </div>
    )
}

Layout.defaultProps = {
    lastThreePosts: [],
    postMetas: [],
    pageMetas: [],
    lastProject: {},
    title: ""
}

export default Layout
