#[derive(Debug)]
pub struct Link {
  icon: String,
  href: String,
  text: String,
}

impl Link {
  pub fn new(icon: Option<&str>, href: &str, text: &str) -> Self {
    return Self {
      icon: icon.unwrap_or("").to_string(),
      href: href.into(),
      text: text.into(),
    };
  }
  pub fn icon(&self) -> &str {
    return &self.icon;
  }
  pub fn href(&self) -> &str {
    return &self.href;
  }
  pub fn text(&self) -> &str {
    return &self.text;
  }
}
