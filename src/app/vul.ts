/* eslint @angular-eslint/directive-selector: off */
import { Directive, OnInit, HostBinding } from '@angular/core';

@Directive({
  selector: '[target="_blank"]',
})
export class Vul implements OnInit {

  @HostBinding('attr.rel') public rel = '';

  public ngOnInit() {
    this.rel = (this.rel || '').split(/\s+/g).concat(
      'noopener', 'noreferrer', 'nofollow'
    ).join(' ').trim();
  }

}
