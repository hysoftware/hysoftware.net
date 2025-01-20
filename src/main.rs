use dioxus::prelude::*;

#[derive(Debug, Clone, Routable, PartialEq)]
#[rustfmt::skip]
enum Route {
    #[layout(Navbar)]
    #[route("/")]
    Home {},
    #[route("/blog/:id")]
    Blog { id: i32 },
}

const BOOTSTRAP_CSS: Asset =
  asset!("/node/node_modules/bootstrap/dist/css/bootstrap.css");
const BOOTSTRAP_JS: Asset =
  asset!("/node/node_modules/bootstrap/dist/js/bootstrap.js");

const FONTAWESOME_CSS: Asset =
  asset!("/node/node_modules/@fortawesome/fontawesome-svg-core/styles.css");
const FONTAWESOME_JS: Asset =
  asset!("/node/node_modules/@fortawesome/fontawesome-svg-core/index.js");

const FAVICON: Asset = asset!("/assets/favicon.ico");
const MAIN_CSS: Asset = asset!("/assets/main.css");

fn main() {
  dioxus::launch(App);
}

#[component]
fn App() -> Element {
  rsx! {
      document::Link { rel: "icon", href: FAVICON }
      document::Link { rel: "stylesheet", href: BOOTSTRAP_CSS }
      document::Link { rel: "stylesheet", href: MAIN_CSS }
      document::Link { rel: "stylesheet", href: FONTAWESOME_CSS }
      document::Link { rel: "stylesheet", href: "https://fonts.googleapis.com/css?family=Roboto:300,400,500" }
      document::Script { src: BOOTSTRAP_JS, defer: true, async: true }
      document::Script { src: FONTAWESOME_JS, defer: true, async: true }
      Router::<Route> {}
  }
}

#[component]
pub fn Hero() -> Element {
  rsx! {
      div {
          id: "hero",
          div { id: "links",
              a { href: "https://dioxuslabs.com/learn/0.6/", "📚 Learn Dioxus" }
              a { href: "https://dioxuslabs.com/awesome", "🚀 Awesome Dioxus" }
              a { href: "https://github.com/dioxus-community/", "📡 Community Libraries" }
              a { href: "https://github.com/DioxusLabs/sdk", "⚙️ Dioxus Development Kit" }
              a { href: "https://marketplace.visualstudio.com/items?itemName=DioxusLabs.dioxus", "💫 VSCode Extension" }
              a { href: "https://discord.gg/XgGxMSkvUM", "👋 Community Discord" }
          }
      }
  }
}

/// Home page
#[component]
fn Home() -> Element {
  rsx! {
      Hero {}

  }
}

/// Blog page
#[component]
pub fn Blog(id: i32) -> Element {
  rsx! {
      div {
          id: "blog",

          // Content
          h1 { "This is blog #{id}!" }
          p { "In blog #{id}, we show how the Dioxus router works and how URL parameters can be passed as props to our route components." }

          // Navigation links
          Link {
              to: Route::Blog { id: id - 1 },
              "Previous"
          }
          span { " <---> " }
          Link {
              to: Route::Blog { id: id + 1 },
              "Next"
          }
      }
  }
}

/// Shared navbar component.
#[component]
fn Navbar() -> Element {
  rsx! {
      div {
          id: "navbar",
          Link {
              to: Route::Home {},
              "Home"
          }
          Link {
              to: Route::Blog { id: 1 },
              "Blog"
          }
      }

      Outlet::<Route> {}
  }
}