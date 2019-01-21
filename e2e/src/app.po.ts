import { browser, by, element } from 'protractor';

export class AppPage {
  navigateTo() {
    return browser.get('/');
  }

  getSNSLinks() {
    return element.all(by.exactRepeater('let item of snsList'));
  }

  getMiscLinks() {
    return element.all(by.exactRepeater('let item of misc'));
  }
}
