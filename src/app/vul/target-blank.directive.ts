import { Directive, OnInit, HostBinding } from '@angular/core';

@Directive({
  selector: '[target="_blank"]',
})
export class TargetBlankDirective implements OnInit {
  @HostBinding('attr.rel') public rel: string;

  constructor() {}

  public ngOnInit() {
    this.rel = (this.rel || '').split(/\s+/g).concat(
      'noopener', 'noreferrer', 'nofollow'
    ).join(' ').trim();
  }
}
