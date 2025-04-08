use ::std::sync::Arc;

use crate::icon::Icons;
use crate::links::Link;

pub struct Ctrl {
  links: Vec<Arc<Link>>,
}

impl Ctrl {
  pub fn new() -> Self {
    return Self {
      links: vec![
        Arc::new(Link::new(
          Icons::FaFileCode.into(),
          "https://github.com/hysoftware/hysoftware.net",
          "_blank",
          "Code of This Page",
        )),
        Arc::new(Link::new(
          Icons::FaFile.into(),
          "https://www.canva.com/design/DADks8eRENo/4npkcNMd5b5OSyFNTXXMvw/view",
          "_blank",
          "Resume about Me",
        )),
      ],
    };
  }

  pub fn links(&self) -> &Vec<Arc<Link>> {
    &self.links
  }
}
