mod icon;
mod links;
mod normal;
mod sns;

use crate::normal::Normal;
use ::dioxus::prelude::*;

#[derive(Debug, Clone, Routable, PartialEq)]
#[rustfmt::skip]
enum Route {
    #[layout(Navbar)]
    #[route("/")]
    Home {},
}

const BOOTSTRAP_CSS: Asset =
  asset!("/node/node_modules/bootstrap/dist/css/bootstrap.css");
const BOOTSTRAP_JS: Asset =
  asset!("/node/node_modules/bootstrap/dist/js/bootstrap.bundle.js");

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
      document::Link { rel: "stylesheet", href: "https://fonts.googleapis.com/css?family=Roboto:300,400,500" }
      document::Link { rel: "stylesheet", href: MAIN_CSS }

      document::Script { src: BOOTSTRAP_JS, defer: true}
      Router::<Route> {}
  }
}

/// Home page
#[component]
fn Home() -> Element {
  rsx! {
    div{
      class: "page",
      div {
        class: "container",
        Normal{}
      }
    }
  }
}

/// Shared navbar component.
#[component]
fn Navbar() -> Element {
  rsx! {
      // div {
      //     id: "navbar",
      //     Link {
      //         to: Route::Home {},
      //         "Home"
      //     }
      //     Link {
      //         to: Route::Blog { id: 1 },
      //         "Blog"
      //     }
      // }

      Outlet::<Route> {}
  }
}
